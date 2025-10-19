```json
{
  "id": "8f43da807f07bb5d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289233,
  "host_pid": "9e6742732c60:1",
  "hash": "c207e3a7bb112dfc48168a489ee2ed8b642e8f940d51ef478e11c34a2dc3ac58",
  "cid": "QmV1c207e3a7bb112dfc48168a489ee2ed8b642e8f94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289233,
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
      "evaluated_at": 1760289233
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
  "sig": "675cb4f272af98c20ad20e72cc8e3743840ff61f884aef2f57f42defaace71fc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279234721
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 26958204, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285764, 'matching_hash': 'a4a7a8ef6540eadb'}}}