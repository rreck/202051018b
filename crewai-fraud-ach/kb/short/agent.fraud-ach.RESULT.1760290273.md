```json
{
  "id": "3ab061df90ac13d0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290273,
  "host_pid": "9e6742732c60:1",
  "hash": "99a85f98b6e0259deca844c7fcf5b86536e5669d3785c55c48991ac63fe7cd32",
  "cid": "QmV199a85f98b6e0259deca844c7fcf5b86536e5669d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290273,
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
      "evaluated_at": 1760290273
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
  "sig": "af058a15607888529c8e00aae6f395493b771e7c1bf0f18b5ebc85cdcf5bdd87"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028289114
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 17352976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285764, 'matching_hash': '2ad1c8bf27fe5526'}}}