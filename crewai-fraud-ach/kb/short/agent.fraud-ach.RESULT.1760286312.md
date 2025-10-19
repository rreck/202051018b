```json
{
  "id": "7fa033c3579b5c80",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286312,
  "host_pid": "9e6742732c60:1",
  "hash": "a1362c977a6c229700a4a9687096d03921cec17cfcb374c6bcfeade233a46f20",
  "cid": "QmV1a1362c977a6c229700a4a9687096d03921cec17c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286312,
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
      "evaluated_at": 1760286312
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
  "sig": "1384ee6620c295d35399e648e6268cbb534672b8a1f507d6ecad2392abf8b6b1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000032270621
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285764, 'matching_hash': '380f2fccd8369f51'}}}