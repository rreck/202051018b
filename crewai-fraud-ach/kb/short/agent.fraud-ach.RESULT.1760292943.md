```json
{
  "id": "9a6c79c7f881294f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292943,
  "host_pid": "9e6742732c60:1",
  "hash": "66186e0c77ba6e86313b960db2ebb241f907c4a17de56f88f7b240e1d0d74e17",
  "cid": "QmV166186e0c77ba6e86313b960db2ebb241f907c4a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292943,
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
      "evaluated_at": 1760292943
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
  "sig": "cd285dc333f36821f8e6bb01f8bd25e820d971708c87d00e5d360b945229ad0e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155104424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 59835776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': 'b81635ada84cf521'}}}maly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5062727}}}