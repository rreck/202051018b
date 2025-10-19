```json
{
  "id": "70b0aa7840ae4804",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285956,
  "host_pid": "9e6742732c60:1",
  "hash": "5061031d3683cfb5cc326ad3c2deb34e487a52484cd85ecacc62d3137d7c02ce",
  "cid": "QmV15061031d3683cfb5cc326ad3c2deb34e487a5248",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285956,
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
      "evaluated_at": 1760285956
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
  "sig": "5a064624d228bc03776621976fd17f5af3aa2ba556431804f18e742cf7c69177"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105150741223
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285765, 'matching_hash': '3a8aff16771fc05f'}}}