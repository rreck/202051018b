```json
{
  "id": "7df844443d8b6d32",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290020,
  "host_pid": "9e6742732c60:1",
  "hash": "aa54f496e55edb31c7f1f1eebe3c69d9258d231b52689e5c8cd305c3e378da79",
  "cid": "QmV1aa54f496e55edb31c7f1f1eebe3c69d9258d231b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290020,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760290020
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "77cc545600de55510512aeaa5a171261c15f9dddca4d03391214585ff18a6636"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021053905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 35371330, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285764, 'matching_hash': '608646e34fdf4d5c'}}}