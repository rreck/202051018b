```json
{
  "id": "71fa0f41f64df528",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288831,
  "host_pid": "9e6742732c60:1",
  "hash": "e25dbf166ed37248148e205fa26597424f8ec70cf7156064dedcdce3ca26c05e",
  "cid": "QmV1e25dbf166ed37248148e205fa26597424f8ec70c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288831,
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
      "evaluated_at": 1760288831
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
  "sig": "4712ae8de428cec654010e57148203a30135c7ddedd163cb1c879d8768e51547"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271527804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 51632700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285764, 'matching_hash': '5c006846cf6d606a'}}}