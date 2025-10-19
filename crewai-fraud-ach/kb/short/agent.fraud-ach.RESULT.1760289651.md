```json
{
  "id": "81934ca3791bc74b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289651,
  "host_pid": "9e6742732c60:1",
  "hash": "67c7a5569e51ec272b1b3f1107ed7a04bfdbfcc54097ce8729d08084df7e2c33",
  "cid": "QmV167c7a5569e51ec272b1b3f1107ed7a04bfdbfcc5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289651,
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
      "evaluated_at": 1760289651
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
  "sig": "600a3b03f378bcd6cbc02a80bfbafabe59c0722ce18c679863b40f26f3cabb4d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272952668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 22838031, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': 'e2aecc84b992b480'}}}