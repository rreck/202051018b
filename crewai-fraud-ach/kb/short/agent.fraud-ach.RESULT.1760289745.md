```json
{
  "id": "5751278a28abff7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289745,
  "host_pid": "9e6742732c60:1",
  "hash": "67beaca9f02d78c5b5a19c1197be73d78c7bf5e8f1f83b904bfb3136f94d2baf",
  "cid": "QmV167beaca9f02d78c5b5a19c1197be73d78c7bf5e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289745,
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
      "evaluated_at": 1760289745
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
  "sig": "a2a4654d4ceba2894bb9e93173ea94f0af8b133b2f63b455e790c554769d3cd2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034886670
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 18060900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285763, 'matching_hash': 'cbf6d0e6528ee173'}}}