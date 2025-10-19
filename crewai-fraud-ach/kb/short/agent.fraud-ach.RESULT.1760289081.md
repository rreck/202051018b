```json
{
  "id": "e797d3cd9437a069",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289081,
  "host_pid": "9e6742732c60:1",
  "hash": "0044dcd06946895b48e0afdee7958b5576de8191b42a6514fd09bf0dce194fd4",
  "cid": "QmV10044dcd06946895b48e0afdee7958b5576de8191",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289081,
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
      "evaluated_at": 1760289081
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
  "sig": "c910be0dd8aa3df9de8021f8e575028c2414a361e1edc2e86475eeb289ef143c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467386779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 28250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': 'cfffbd2ec30a8ce4'}}}