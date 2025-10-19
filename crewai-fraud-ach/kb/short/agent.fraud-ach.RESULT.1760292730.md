```json
{
  "id": "d5ce9ad4433a768a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292730,
  "host_pid": "9e6742732c60:1",
  "hash": "27584822dcb4ff2feb2b58fc21a4efc3c7754400594a0f0d36a70d9bd261dda4",
  "cid": "QmV127584822dcb4ff2feb2b58fc21a4efc3c7754400",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292730,
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
      "evaluated_at": 1760292730
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
  "sig": "b51af95141aed37e51c34da76bccbb4843be22b7d14115c24d78cbbbae552c5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150868994
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 84541068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '612406b6271445a9'}}}