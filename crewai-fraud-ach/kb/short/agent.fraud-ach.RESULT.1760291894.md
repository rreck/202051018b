```json
{
  "id": "ed9029ef0c087457",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291894,
  "host_pid": "9e6742732c60:1",
  "hash": "a1e2b2fe9f4177558cc07be89141cbadc8d8dbff7c69ecfe8dcfbebcf7322e6a",
  "cid": "QmV1a1e2b2fe9f4177558cc07be89141cbadc8d8dbff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291894,
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
      "evaluated_at": 1760291894
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
  "sig": "604f03c0d050ee1345906f50fb3bbc14a30ab5aeda4bd2150762080718ffebc9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021480535
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 91250695, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285765, 'matching_hash': '9682be52dcbb3d1d'}}}