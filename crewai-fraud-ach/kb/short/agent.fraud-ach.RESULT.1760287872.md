```json
{
  "id": "05ed2b780aa33dee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287872,
  "host_pid": "9e6742732c60:1",
  "hash": "27ae37149c42095ae5eb0b5ba38cca9a49a2abd6162fc64879875a99a2d858ba",
  "cid": "QmV127ae37149c42095ae5eb0b5ba38cca9a49a2abd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287872,
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
      "evaluated_at": 1760287872
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
  "sig": "1690b800b3a2aea2b331ebff3473cf4afd3d3ed0d36dba57bb13044ab6b30c43"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024300942
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285763, 'matching_hash': '95903848ba405d51'}}}een': 1760285763, 'matching_hash': '04117a7715fe8402'}}}}}