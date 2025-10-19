```json
{
  "id": "d8be0f028da2cbf0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293034,
  "host_pid": "9e6742732c60:1",
  "hash": "88ed8594140186e7ea8d8e845231de56582954bd59fd683ba812cc78f105dbd7",
  "cid": "QmV188ed8594140186e7ea8d8e845231de56582954bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293034,
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
      "evaluated_at": 1760293034
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
  "sig": "79a57eeed50749245412fd2b4a4226ed2ae65e380be0295267b7ee99fef39451"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 12412890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}