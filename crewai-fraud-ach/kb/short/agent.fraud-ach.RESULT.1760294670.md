```json
{
  "id": "417fed29f87d0355",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294670,
  "host_pid": "9e6742732c60:1",
  "hash": "5b577810e39856f60c550e70e7a51cfdbb2bd9ba682b11fd183aa94453e14942",
  "cid": "QmV15b577810e39856f60c550e70e7a51cfdbb2bd9ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294670,
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
      "evaluated_at": 1760294670
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
  "sig": "665b6fa53a08b0752972fdbc4897153dc0b833aca02311ae4363593c3a950ec1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245772760
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 16017980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}