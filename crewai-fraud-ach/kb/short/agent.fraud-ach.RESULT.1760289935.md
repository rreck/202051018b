```json
{
  "id": "32cc7095a7eb1535",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289935,
  "host_pid": "9e6742732c60:1",
  "hash": "d72024a4fe78115a096f895c7ff7d565db7428551fa0b5337e2928ad81645b25",
  "cid": "QmV1d72024a4fe78115a096f895c7ff7d565db742855",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289935,
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
      "evaluated_at": 1760289935
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
  "sig": "ba10d16fb6078c828cad50dc4cf77251a8db25f1d9b73676d3ade60f9ea7b9aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150369382
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 49019696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '1d04175be49b6deb'}}}