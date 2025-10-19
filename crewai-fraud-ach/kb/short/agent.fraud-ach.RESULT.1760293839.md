```json
{
  "id": "a5f80fbd29c73cbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293839,
  "host_pid": "9e6742732c60:1",
  "hash": "f2bc29fa2e2ea9f04ac5270820934e866cd412a7486157f3ff87c33fe063d31d",
  "cid": "QmV1f2bc29fa2e2ea9f04ac5270820934e866cd412a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293839,
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
      "evaluated_at": 1760293839
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
  "sig": "639017e6968d4b833ad2fe36f1119ed14596904c4e459e5e072567de3449981a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599169809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 65877192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': '606495659f158f1b'}}}