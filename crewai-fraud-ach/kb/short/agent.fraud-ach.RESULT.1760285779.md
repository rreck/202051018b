```json
{
  "id": "42f93f95b9913116",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285779,
  "host_pid": "9e6742732c60:1",
  "hash": "4210ed0ac92432e525ec0157941173b2953378a60ed20f57afaeff0d443c9f58",
  "cid": "QmV14210ed0ac92432e525ec0157941173b2953378a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285779,
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
      "evaluated_at": 1760285779
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
  "sig": "32778438c2f6c7ac41c109ed3084d318aceb6c900575500ea7877afe4e1718ad"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105151200756
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285763, 'matching_hash': 'e0249734267f8906'}}}