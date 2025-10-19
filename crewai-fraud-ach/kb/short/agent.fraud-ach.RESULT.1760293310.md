```json
{
  "id": "46160d4607bdcdda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293310,
  "host_pid": "9e6742732c60:1",
  "hash": "2f7ce736d65c9c878a863f360aba94f17f108ed30dc101b04a2703467a9d3417",
  "cid": "QmV12f7ce736d65c9c878a863f360aba94f17f108ed3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293310,
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
      "evaluated_at": 1760293310
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
  "sig": "5a175d912fa7cff8623edfcb57e654e4fa4b1338089a431add356e7c734e3417"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027741847
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 24906312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '4cdb4cc94f6cfd73'}}}