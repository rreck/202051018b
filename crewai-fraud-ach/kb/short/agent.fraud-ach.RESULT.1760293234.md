```json
{
  "id": "6ff3e47fa6399a47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293234,
  "host_pid": "9e6742732c60:1",
  "hash": "a8c5713eb5cf115dc22ccc3ab50c61e64ba1b031e15ab9c0952bdf985b73d049",
  "cid": "QmV1a8c5713eb5cf115dc22ccc3ab50c61e64ba1b031",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293234,
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
      "evaluated_at": 1760293234
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
  "sig": "f2f7b19f9ab788eff1028d8d1d00750b499033a49d8ccdec2abf12d0e21eefa7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460464182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 22604606, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285765, 'matching_hash': '97f231b14306ced8'}}}