```json
{
  "id": "43fd829bbe65e2d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289538,
  "host_pid": "9e6742732c60:1",
  "hash": "455e7e4886299eca47bb3e35fa5c00e2b324b496a284deae917b29b52be36100",
  "cid": "QmV1455e7e4886299eca47bb3e35fa5c00e2b324b496",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289538,
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
      "evaluated_at": 1760289538
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
  "sig": "a4f0a1ed1c0617e36e071fb36b1ffef20785ae2fe143528caea4a89df4086b11"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277046981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 39076380, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '189e75bc7166d961'}}}