```json
{
  "id": "3be1b0157349b507",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288540,
  "host_pid": "9e6742732c60:1",
  "hash": "d70791a1f91b10aedd870f20810a6034f72e2c7153cadef041fa471f447e2b3d",
  "cid": "QmV1d70791a1f91b10aedd870f20810a6034f72e2c71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288540,
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
      "evaluated_at": 1760288540
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
  "sig": "d6d93573d0593d559906c3f6c7bf45ca6745a555a8f500e2a7aab34e0734ba74"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469007601
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285765, 'matching_hash': '9208fda71b3c290c'}}}