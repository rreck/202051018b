```json
{
  "id": "94d4d160a4f3f1fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286925,
  "host_pid": "9e6742732c60:1",
  "hash": "92410aa2a350d58aabe5eb651847446335171af47c998878d7a325c3c233e999",
  "cid": "QmV192410aa2a350d58aabe5eb651847446335171af4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286925,
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
      "evaluated_at": 1760286925
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
  "sig": "920c7ae2f0245c32795d7678fb75abd8844138aff3071121db1708a6730f5d07"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100279304140
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285764, 'matching_hash': '56d1c75d448f4ea1'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285764, 'matching_hash': '75b6b5cd12274a09'}}}