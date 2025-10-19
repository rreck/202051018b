```json
{
  "id": "969f12520e7f8a1b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292283,
  "host_pid": "9e6742732c60:1",
  "hash": "d0a50ddfbfe7112c725ada3f14256a1798110ab9c5020d818aea954c869f8055",
  "cid": "QmV1d0a50ddfbfe7112c725ada3f14256a1798110ab9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292283,
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
      "evaluated_at": 1760292283
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
  "sig": "79b11aa75d500c226375e01615bc16a84b488daa4d46155275a961528fe03728"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245017605
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 91262644, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '04117a7715fe8402'}}}