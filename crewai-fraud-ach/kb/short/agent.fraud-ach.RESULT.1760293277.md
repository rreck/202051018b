```json
{
  "id": "6249aefefcf5dd57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293277,
  "host_pid": "9e6742732c60:1",
  "hash": "917cd7e774c560c635a800169fbadc1e1b780929a962c27d54eeaed106c5dd32",
  "cid": "QmV1917cd7e774c560c635a800169fbadc1e1b780929",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293277,
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
      "evaluated_at": 1760293277
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
  "sig": "94792ffaf56da9e590302108448f6fd726ef69b3c411aa87327993725fb85b53"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245017605
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 101141590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '04117a7715fe8402'}}}