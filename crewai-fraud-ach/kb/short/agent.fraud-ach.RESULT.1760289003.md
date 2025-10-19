```json
{
  "id": "bd724a140ae5d069",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289003,
  "host_pid": "9e6742732c60:1",
  "hash": "865e47ffdbc4af7f401c27412a3e47095678e4a17b980b3567d517941af7539c",
  "cid": "QmV1865e47ffdbc4af7f401c27412a3e47095678e4a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289003,
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
      "evaluated_at": 1760289003
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
  "sig": "fc6473ccb866d3ea437cd770fc2dc10ac7aef2eebfe04c4e956e25514e6cd901"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 35007280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}