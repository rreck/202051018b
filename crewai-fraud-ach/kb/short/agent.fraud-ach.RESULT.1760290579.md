```json
{
  "id": "77ea69e805603f56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290579,
  "host_pid": "9e6742732c60:1",
  "hash": "1c81f1eb798f03753cc7d18d9b4b9cdab022b8c958077dda5bd50241cbd2e944",
  "cid": "QmV11c81f1eb798f03753cc7d18d9b4b9cdab022b8c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290579,
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
      "evaluated_at": 1760290579
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
  "sig": "e537df8b4ea730982d0d2443c7b8719539c909f80d0258987cd988068ac99d4f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462755939
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 13486858, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285764, 'matching_hash': '0ef039381f9434ef'}}}