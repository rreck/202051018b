```json
{
  "id": "2054a610f353aa8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292279,
  "host_pid": "9e6742732c60:1",
  "hash": "fe7734b804ef71601c9d7f43831eb573c3656404f4851c7031bec555ce30e9f6",
  "cid": "QmV1fe7734b804ef71601c9d7f43831eb573c3656404",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292279,
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
      "evaluated_at": 1760292279
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
  "sig": "b412ee36ecb1388be343505650eca889e4bdedeb20431dbaca15b64530669dfb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020376030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 73361876, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '92ff62b724ca331a'}}}