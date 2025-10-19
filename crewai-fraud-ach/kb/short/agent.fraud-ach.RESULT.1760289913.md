```json
{
  "id": "00b41b1fa9fdd5cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289913,
  "host_pid": "9e6742732c60:1",
  "hash": "2ec1b90f50a2a7dd8ce50d45314346b8646a3f78f625e8e8c120b49bba7d8c7f",
  "cid": "QmV12ec1b90f50a2a7dd8ce50d45314346b8646a3f78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289913,
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
      "evaluated_at": 1760289913
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
  "sig": "487648c277bab17db7905d2c7590a465ca4803984b8aa649fab9c04eb2921a33"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034020503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285765, 'matching_hash': '8db66b2beb557931'}}}