```json
{
  "id": "ed66bb7db0293fec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288683,
  "host_pid": "9e6742732c60:1",
  "hash": "615c3fe6b30b49d1b26e11fd395940eda1a251ec739e8c3209287ad259521e3c",
  "cid": "QmV1615c3fe6b30b49d1b26e11fd395940eda1a251ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288683,
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
      "evaluated_at": 1760288683
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
  "sig": "1c6de8efc6a101b4bc1ef172da3b09745ca4eb28bf865e6e4dcd4089699b2dfd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596004100
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 16040921, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': '0723803785cdf871'}}}