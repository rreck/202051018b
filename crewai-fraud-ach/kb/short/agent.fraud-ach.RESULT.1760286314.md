```json
{
  "id": "d2b0a70b358cc68c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286314,
  "host_pid": "9e6742732c60:1",
  "hash": "55feffbd95c5577a5bbace3dd68e54ae60ed22a77b95011e9585aed638b16d75",
  "cid": "QmV155feffbd95c5577a5bbace3dd68e54ae60ed22a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286314,
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
      "evaluated_at": 1760286314
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
  "sig": "8c948f63d734a941fa69d77b0d171904f607c7d2559dfa30ea654c978265b9cf"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105150676701
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285765, 'matching_hash': 'f947c72340b5e951'}}}