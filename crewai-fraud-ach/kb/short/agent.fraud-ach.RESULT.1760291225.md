```json
{
  "id": "8570a5ea6c0725e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291225,
  "host_pid": "9e6742732c60:1",
  "hash": "87e6041831596c217643fe00e40bad2b7759f8b6af1d37255a435e4fe7759ba7",
  "cid": "QmV187e6041831596c217643fe00e40bad2b7759f8b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291225,
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
      "evaluated_at": 1760291225
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
  "sig": "984f1b5a04b4b816d46dee7b87f354ebd4d8aed1db40360470d97b76df657fdf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154917617
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 71522570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'bb8a68e9925b6436'}}}