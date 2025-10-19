```json
{
  "id": "58048a6206cb30f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288824,
  "host_pid": "9e6742732c60:1",
  "hash": "2cdb28edc760d49c84d0e56b47d74793ddf41377a447f5d4d42e9f889bb241e0",
  "cid": "QmV12cdb28edc760d49c84d0e56b47d74793ddf41377",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288824,
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
      "evaluated_at": 1760288824
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
  "sig": "5de97709bfd82dcd7a14f1cd6b4549521bb8e14804ad8f71f9ce6db41acc7267"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029664164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 49307895, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285764, 'matching_hash': '915cdda6adcb6880'}}}