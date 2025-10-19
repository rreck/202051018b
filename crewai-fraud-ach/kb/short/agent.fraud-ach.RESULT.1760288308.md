```json
{
  "id": "3ac65428f1974c2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288308,
  "host_pid": "9e6742732c60:1",
  "hash": "2d21515efbdc2013a95e4102923128795df36ca4f4c76ab5a16983d534ae83c3",
  "cid": "QmV12d21515efbdc2013a95e4102923128795df36ca4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288308,
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
      "evaluated_at": 1760288308
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
  "sig": "5e60b8d6f17d52400057a701aa49343921d5a590ae5525ef6783ee7646a42ed9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029265266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 32671277, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285764, 'matching_hash': 'a9619dd56a360910'}}}