```json
{
  "id": "c21efbe161cb46ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290998,
  "host_pid": "9e6742732c60:1",
  "hash": "3cefa000a952e44babb3521296cf835e13d24763e86c8a779d824392d0b6d177",
  "cid": "QmV13cefa000a952e44babb3521296cf835e13d24763",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290998,
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
      "evaluated_at": 1760290998
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
  "sig": "a3851636670cd35643a20f0d939a8933d7680666ac79f7e5ac5e1e409cdbab7c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590866940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 69699344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}