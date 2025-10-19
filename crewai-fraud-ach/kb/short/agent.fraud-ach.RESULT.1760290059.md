```json
{
  "id": "0e2a694a533ca7c7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290059,
  "host_pid": "9e6742732c60:1",
  "hash": "8e8d4362b15ab38790611cccdb9670f7c8e725d9b2ace1c55efad8f1d16fa439",
  "cid": "QmV18e8d4362b15ab38790611cccdb9670f7c8e725d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290059,
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
      "evaluated_at": 1760290059
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
  "sig": "e07da9fa2134e4854ef07d811283e2c8d011b2815fb4226b763cf437cd502063"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151957108
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 67486160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285765, 'matching_hash': 'c64e753eaec43197'}}}