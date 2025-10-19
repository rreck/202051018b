```json
{
  "id": "a2f68e593a93d98d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286547,
  "host_pid": "9e6742732c60:1",
  "hash": "69db8a3746cdd5003d9fa2ce377af228086022678a4ff647161b06992e127183",
  "cid": "QmV169db8a3746cdd5003d9fa2ce377af22808602267",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286547,
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
      "evaluated_at": 1760286547
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "bb97ca17ee8db9e827aa1e445f4aa0bb96eca5c3a062a7965d94149cd19d9898"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000036798243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12820668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': '9f3869b775bbb8aa'}}}