```json
{
  "id": "70579981791472c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291790,
  "host_pid": "9e6742732c60:1",
  "hash": "aacc6bc8168533d6789006f44cefc15fc37b08fa311c2d5cc50fbfbcb55b68f6",
  "cid": "QmV1aacc6bc8168533d6789006f44cefc15fc37b08fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291790,
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
      "evaluated_at": 1760291790
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
  "sig": "a1275eaf5df60cb312f153989459c04158234c635c8016e2863015438af9145c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029233033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 75987822, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': 'f6bf3c76ea3935d9'}}}