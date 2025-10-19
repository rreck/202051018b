```json
{
  "id": "df5cc67a6a66e727",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286809,
  "host_pid": "9e6742732c60:1",
  "hash": "740591dc37900e735dbfd3c1458dec4db42e8ffc697f2e16abaa8117c3005654",
  "cid": "QmV1740591dc37900e735dbfd3c1458dec4db42e8ffc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286809,
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
      "evaluated_at": 1760286809
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8e2215ce19e228b998db30b0d0d2e0954c07852ac1aca049c29f182bd71b1870"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009592795708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17466738, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285763, 'matching_hash': '6f9672c314113419'}}}