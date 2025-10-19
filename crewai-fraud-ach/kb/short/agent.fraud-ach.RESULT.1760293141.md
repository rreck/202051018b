```json
{
  "id": "cf9cb16bf580b762",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293141,
  "host_pid": "9e6742732c60:1",
  "hash": "2112e13769efb1bbb611526b71220d0d96512adf6414d530099186fb96a06d5b",
  "cid": "QmV12112e13769efb1bbb611526b71220d0d96512adf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293141,
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
      "evaluated_at": 1760293141
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
  "sig": "671bac82f7e8920cd620da9f7ec9aa17b2dd1d3c063d0af45df4c8d3fd2846d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159090424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 36662644, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285764, 'matching_hash': 'fe78f8ea626833d8'}}}