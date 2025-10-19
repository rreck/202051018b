```json
{
  "id": "5bebb7caa08c5428",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292466,
  "host_pid": "9e6742732c60:1",
  "hash": "b456abfcc540bcaf92ab7b3733eda876734de1dbd2b936d750b9121888a1201f",
  "cid": "QmV1b456abfcc540bcaf92ab7b3733eda876734de1db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292466,
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
      "evaluated_at": 1760292466
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
  "sig": "f1a81fed8450d802c8139c64320ab9f8c62c8c8d2de0eea2f1f9bdddf1e1286a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029664164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 92980602, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285764, 'matching_hash': '915cdda6adcb6880'}}}