```json
{
  "id": "0b6560753e63f5da",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288988,
  "host_pid": "9e6742732c60:1",
  "hash": "1087e49fb0a7e1a5e9eeacae8c3aeb25b8c63a07f294643f564b63d8709671f5",
  "cid": "QmV11087e49fb0a7e1a5e9eeacae8c3aeb25b8c63a07",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288988,
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
      "evaluated_at": 1760288988
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
  "sig": "5c3e3e809580a70f06dba0796103c064317eef340f024519e8e48c94f4d5a02d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154261308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285763, 'matching_hash': 'f5aec8f7458ab0e7'}}}een': 1760285764, 'matching_hash': '8e78dc9e18bacaa7'}}}