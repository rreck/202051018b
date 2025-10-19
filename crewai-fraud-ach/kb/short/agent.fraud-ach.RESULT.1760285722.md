```json
{
  "id": "c8760f135e1495d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285722,
  "host_pid": "9e6742732c60:1",
  "hash": "51c1d1254258faf3ed95ba31b8f3bb81defef364f48eddc6a8c69c007f252320",
  "cid": "QmV151c1d1254258faf3ed95ba31b8f3bb81defef364",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285722,
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
      "evaluated_at": 1760285722
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
  "sig": "5aa5134f23daa274492921015c178ab20d0e58bcce4da4719a2febec15368112"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 30761762, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}