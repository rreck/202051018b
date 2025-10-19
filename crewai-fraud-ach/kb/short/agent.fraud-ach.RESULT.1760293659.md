```json
{
  "id": "23a37d3b23eaf703",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293659,
  "host_pid": "9e6742732c60:1",
  "hash": "7c67d98248d263922efcb10f7604e272544212a1d0a835188f7f7593990b0967",
  "cid": "QmV17c67d98248d263922efcb10f7604e272544212a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293659,
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
      "evaluated_at": 1760293659
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
  "sig": "49027fa3471150ff9623e8d76d17b4302d94e9f29063b545220c682273327f0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021151885
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 54608463, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285764, 'matching_hash': '925ef0ca9f93e495'}}}