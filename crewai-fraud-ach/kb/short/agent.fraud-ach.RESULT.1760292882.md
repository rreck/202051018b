```json
{
  "id": "836fb5ccd475fccb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292882,
  "host_pid": "9e6742732c60:1",
  "hash": "82193ee84369bd7b35201e8c62c2227ffbb7c1e1865f9639677a19b25f1b2a34",
  "cid": "QmV182193ee84369bd7b35201e8c62c2227ffbb7c1e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292882,
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
      "evaluated_at": 1760292882
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
  "sig": "b6f14b4cad2f87b064ade2841260165cd91906084f474188fb5e1c06c84196cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153135421
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 78998652, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '4394c86a949e27d6'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}