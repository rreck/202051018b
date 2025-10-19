```json
{
  "id": "4a386a91d1c51ed7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294217,
  "host_pid": "9e6742732c60:1",
  "hash": "59c399cd04d3ecb585d40d3dc80d743412bb079df10ac544e5c121d9236effd6",
  "cid": "QmV159c399cd04d3ecb585d40d3dc80d743412bb079d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294217,
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
      "evaluated_at": 1760294217
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
  "sig": "04b996f4b245f2a33dc20b1c9d3c111a375fff54f7f67ead03c92b177a390434"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150868994
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 96973578, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '612406b6271445a9'}}}