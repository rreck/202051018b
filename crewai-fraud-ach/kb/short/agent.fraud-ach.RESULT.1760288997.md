```json
{
  "id": "a0454ce0a10ce88a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288997,
  "host_pid": "9e6742732c60:1",
  "hash": "49c3d57942ff87a9f6c54f5cad4281a88a2fea3fbe4af1ece8feddc89f2afc36",
  "cid": "QmV149c3d57942ff87a9f6c54f5cad4281a88a2fea3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288997,
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
      "evaluated_at": 1760288997
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
  "sig": "d993f7ebcbbc3a444b67222e19fab87a3fb13871ab8a221de14d7955cf11847c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029441717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 23409980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285764, 'matching_hash': 'f6bac04718607b3a'}}}