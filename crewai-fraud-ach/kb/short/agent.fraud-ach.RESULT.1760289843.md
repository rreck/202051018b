```json
{
  "id": "eb79194569161b34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289843,
  "host_pid": "9e6742732c60:1",
  "hash": "2cfba321c5ae9e2070310f0fcf2dc84b814a6def4e6fe91193b40f284b16e034",
  "cid": "QmV12cfba321c5ae9e2070310f0fcf2dc84b814a6def",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289843,
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
      "evaluated_at": 1760289843
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
  "sig": "07b968a6c74ae56fb73b72c8869b26622e01f962d19f7ee957090ff49e978948"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 42645232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}