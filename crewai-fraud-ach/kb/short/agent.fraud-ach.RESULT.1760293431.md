```json
{
  "id": "29a45694cd951f33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293431,
  "host_pid": "9e6742732c60:1",
  "hash": "ca3475572f0291c635a888555b1658b756a954fbffe0632c89f7cd274cf9e823",
  "cid": "QmV1ca3475572f0291c635a888555b1658b756a954fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293431,
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
      "evaluated_at": 1760293431
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
  "sig": "8046fd6efb48014a4b94252652b3cf86dc0ea2f7ef85329f9c11c69988644415"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 83049934, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': 'a46c33998c9a26e1'}}}