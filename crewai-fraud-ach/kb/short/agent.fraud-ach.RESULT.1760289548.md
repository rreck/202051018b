```json
{
  "id": "6e20726098a4abf1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289548,
  "host_pid": "9e6742732c60:1",
  "hash": "4559ded0700ab95e44e56d9a1c314006be36d0dddd304d73bdbb497ba12c1e8f",
  "cid": "QmV14559ded0700ab95e44e56d9a1c314006be36d0dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289548,
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
      "evaluated_at": 1760289548
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
  "sig": "d21112780fc62ef73e8f30f19a89838282e87f3a971f835894591ec4755d7e4b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240153207
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 31500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285764, 'matching_hash': '9e24c0ed91a48db3'}}}