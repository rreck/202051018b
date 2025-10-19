```json
{
  "id": "499f112d514069f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290024,
  "host_pid": "9e6742732c60:1",
  "hash": "5c1268e0b0ecfdfb04e4e91a5eb504f59c9fd725ec745693d16acfee2d0ff508",
  "cid": "QmV15c1268e0b0ecfdfb04e4e91a5eb504f59c9fd725",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290024,
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
      "evaluated_at": 1760290024
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
  "sig": "85c80e07a66cb2abf13d5078d2bbf97de44cd3945dbccf1b223ee7c7c3f5ec86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 38449763, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285765, 'matching_hash': 'a63e704272eccc25'}}}