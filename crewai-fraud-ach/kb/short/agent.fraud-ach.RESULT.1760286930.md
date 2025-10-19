```json
{
  "id": "4c63467d4075eb21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286930,
  "host_pid": "9e6742732c60:1",
  "hash": "702b5a0981c181a9d020d82277c1a80c635274eb342baa4c1a8a88519ad5da86",
  "cid": "QmV1702b5a0981c181a9d020d82277c1a80c635274eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286930,
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
      "evaluated_at": 1760286930
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
  "sig": "01791d216cb2b9e213177d3c87aa4e574db29c114c9138bb4313b7d1e305dce2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201464550835
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285763, 'matching_hash': '50cb0ee46794e046'}}}