```json
{
  "id": "44454b039afe57dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293881,
  "host_pid": "9e6742732c60:1",
  "hash": "bd60cf68ffb3b38033f9f744b51b1cbfcc83c9ce72b7c8e15af94a50e83ebb9a",
  "cid": "QmV1bd60cf68ffb3b38033f9f744b51b1cbfcc83c9ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293881,
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
      "evaluated_at": 1760293881
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
  "sig": "78c5fef43e4eefb6a864fe0d5b439def31085d9daeacfc434ea7785f853464a8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599036440
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 90558472, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': '93c00e1af0416a0b'}}}