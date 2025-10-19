```json
{
  "id": "7015307fc46b6465",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290983,
  "host_pid": "9e6742732c60:1",
  "hash": "4432c4367ea4b3f10d630238aeca54effd5680089958cd0a5b470ee69132e6a7",
  "cid": "QmV14432c4367ea4b3f10d630238aeca54effd568008",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290983,
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
      "evaluated_at": 1760290983
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
  "sig": "015ade9ea28928d2d38f5585b6ca4dfcf5e10e42af3e6c7d30d1b485541b9d56"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598880520
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 31236096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285764, 'matching_hash': '9fe1b03994749115'}}}